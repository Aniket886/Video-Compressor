#!/usr/bin/env python3
"""
CompressVideo - Desktop Application
A standalone video compression app with modern UI
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
import threading
import json
from pathlib import Path
from datetime import datetime

# Modern color scheme
COLORS = {
    'primary': '#6366f1',
    'primary_dark': '#4f46e5',
    'secondary': '#8b5cf6',
    'success': '#10b981',
    'warning': '#f59e0b',
    'error': '#ef4444',
    'bg_light': '#f8fafc',
    'bg_card': '#ffffff',
    'text_primary': '#0f172a',
    'text_secondary': '#475569',
    'text_muted': '#64748b',
    'border': '#e2e8f0',
}


class CompressVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CompressVideo")
        self.root.geometry("800x700")
        self.root.minsize(700, 600)
        self.root.configure(bg=COLORS['bg_light'])

        # Center window
        self.center_window()

        # Current file info
        self.current_file = None
        self.video_info = None
        self.compression_running = False
        self.cancelled = False

        # FFmpeg path
        self.ffmpeg_path = self.find_ffmpeg()

        # Create styles
        self.create_styles()

        # Build UI
        self.create_ui()

        # Check FFmpeg
        if not self.ffmpeg_path:
            self.show_ffmpeg_error()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = 800
        height = 700
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_styles(self):
        """Create modern ttk styles"""
        style = ttk.Style()

        # Configure base styles
        style.configure('TFrame', background=COLORS['bg_light'])
        style.configure('TLabel', background=COLORS['bg_light'], font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'))

        # Card frame style
        style.configure('Card.TFrame', background=COLORS['bg_card'])
        style.configure('Card.TLabel', background=COLORS['bg_card'])

        # Title label
        style.configure('Title.TLabel',
                       font=('Segoe UI', 24, 'bold'),
                       foreground=COLORS['text_primary'])

        # Subtitle label
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 11),
                       foreground=COLORS['text_secondary'])

        # Primary button
        style.configure('Primary.TButton',
                       font=('Segoe UI', 11, 'bold'),
                       padding=(20, 10))

        # Secondary button
        style.configure('Secondary.TButton',
                       font=('Segoe UI', 10),
                       padding=(15, 8))

    def create_ui(self):
        """Create the user interface"""
        # Main container with padding
        main_container = ttk.Frame(self.root, padding="20")
        main_container.pack(fill=tk.BOTH, expand=True)

        # Header
        self.create_header(main_container)

        # Scrollable content
        self.create_scrollable_content(main_container)

    def create_header(self, parent):
        """Create header section"""
        header = ttk.Frame(parent)
        header.pack(fill=tk.X, pady=(0, 20))

        # Logo and title
        title_frame = ttk.Frame(header)
        title_frame.pack(fill=tk.X)

        # Logo icon (using text)
        logo_label = tk.Label(title_frame, text="▶",
                               font=('Segoe UI', 32),
                               fg=COLORS['primary'],
                               bg=COLORS['bg_light'])
        logo_label.pack(side=tk.LEFT, padx=(0, 10))

        # Title
        title = ttk.Label(title_frame, text="CompressVideo", style='Title.TLabel')
        title.pack(side=tk.LEFT)

        # Subtitle
        subtitle = ttk.Label(header,
                            text="Compress videos up to 10GB while maintaining quality",
                            style='Subtitle.TLabel')
        subtitle.pack(anchor=tk.W, pady=(5, 0))

    def create_scrollable_content(self, parent):
        """Create scrollable content area"""
        # Canvas for scrolling
        self.canvas = tk.Canvas(parent, bg=COLORS['bg_light'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=760)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Bind mouse wheel
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Pack
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create sections
        self.create_upload_section()
        self.create_info_section()
        self.create_settings_section()
        self.create_progress_section()

    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_card(self, parent, title=None):
        """Create a card container"""
        card = tk.Frame(parent, bg=COLORS['bg_card'],
                       highlightbackground=COLORS['border'],
                       highlightthickness=1, bd=0)
        card.pack(fill=tk.X, pady=(0, 15), padx=5)

        # Add shadow effect (using padding)
        inner = tk.Frame(card, bg=COLORS['bg_card'], padx=20, pady=20)
        inner.pack(fill=tk.BOTH, expand=True)

        if title:
            title_label = tk.Label(inner, text=title,
                                  font=('Segoe UI', 14, 'bold'),
                                  fg=COLORS['text_primary'],
                                  bg=COLORS['bg_card'])
            title_label.pack(anchor=tk.W, pady=(0, 15))

        return inner

    def create_upload_section(self):
        """Create upload section"""
        self.upload_frame = self.create_card(self.scrollable_frame)

        # Upload button area
        upload_area = tk.Frame(self.upload_frame, bg=COLORS['bg_card'])
        upload_area.pack(fill=tk.X, pady=20)

        # Upload icon (text symbol)
        icon_label = tk.Label(upload_area, text="📁",
                             font=('Segoe UI', 48),
                             bg=COLORS['bg_card'])
        icon_label.pack(pady=(0, 10))

        # Upload text
        text_label = tk.Label(upload_area, text="Drop your video here or click to browse",
                             font=('Segoe UI', 12),
                             fg=COLORS['text_secondary'],
                             bg=COLORS['bg_card'])
        text_label.pack()

        # Supported formats
        formats_label = tk.Label(upload_area,
                                text="Supports MP4, MOV, AVI, MKV, WebM up to 10GB",
                                font=('Segoe UI', 9),
                                fg=COLORS['text_muted'],
                                bg=COLORS['bg_card'])
        formats_label.pack(pady=(10, 15))

        # Select button
        self.select_btn = tk.Button(upload_area, text="Select Video",
                                   font=('Segoe UI', 11, 'bold'),
                                   bg=COLORS['primary'],
                                   fg='white',
                                   activebackground=COLORS['primary_dark'],
                                   activeforeground='white',
                                   padx=30, pady=12,
                                   cursor='hand2',
                                   relief=tk.FLAT,
                                   command=self.select_file)
        self.select_btn.pack()

        # File name display
        self.file_label = tk.Label(self.upload_frame, text="",
                                  font=('Segoe UI', 10),
                                  fg=COLORS['text_secondary'],
                                  bg=COLORS['bg_card'])
        self.file_label.pack(pady=(10, 0))

    def create_info_section(self):
        """Create video info section"""
        self.info_frame = self.create_card(self.scrollable_frame, "Video Information")
        self.info_frame.pack_forget()  # Hide initially

        # Info grid
        info_grid = tk.Frame(self.info_frame, bg=COLORS['bg_card'])
        info_grid.pack(fill=tk.X)

        # Create info labels
        self.info_labels = {}
        info_items = [
            ('file_name', 'File Name:'),
            ('size', 'Original Size:'),
            ('duration', 'Duration:'),
            ('format', 'Format:'),
            ('resolution', 'Resolution:'),
        ]

        for i, (key, label) in enumerate(info_items):
            row = i // 2
            col = i % 2

            item_frame = tk.Frame(info_grid, bg=COLORS['bg_card'])
            item_frame.grid(row=row, column=col, sticky='w', pady=5, padx=(0, 40))

            label_widget = tk.Label(item_frame, text=label,
                                   font=('Segoe UI', 9),
                                   fg=COLORS['text_muted'],
                                   bg=COLORS['bg_card'])
            label_widget.pack(side=tk.LEFT)

            value_widget = tk.Label(item_frame, text="-",
                                   font=('Segoe UI', 9, 'bold'),
                                   fg=COLORS['text_primary'],
                                   bg=COLORS['bg_card'])
            value_widget.pack(side=tk.LEFT, padx=(5, 0))

            self.info_labels[key] = value_widget

    def create_settings_section(self):
        """Create compression settings section"""
        self.settings_frame = self.create_card(self.scrollable_frame, "Compression Settings")
        self.settings_frame.pack_forget()  # Hide initially

        # Recommendations
        rec_label = tk.Label(self.settings_frame, text="Recommended sizes for this video:",
                            font=('Segoe UI', 10),
                            fg=COLORS['text_secondary'],
                            bg=COLORS['bg_card'])
        rec_label.pack(anchor=tk.W, pady=(0, 10))

        # Recommendation buttons frame
        self.rec_frame = tk.Frame(self.settings_frame, bg=COLORS['bg_card'])
        self.rec_frame.pack(fill=tk.X, pady=(0, 20))

        # Target size
        size_frame = tk.Frame(self.settings_frame, bg=COLORS['bg_card'])
        size_frame.pack(fill=tk.X, pady=(0, 15))

        size_label = tk.Label(size_frame, text="Target Size:",
                             font=('Segoe UI', 10, 'bold'),
                             fg=COLORS['text_primary'],
                             bg=COLORS['bg_card'])
        size_label.pack(anchor=tk.W)

        self.size_var = tk.StringVar(value="100")
        size_options = ["50", "100", "250", "500", "1000", "2000", "5000", "custom"]
        size_names = ["50 MB", "100 MB", "250 MB", "500 MB", "1 GB", "2 GB", "5 GB", "Custom"]

        self.size_menu = ttk.Combobox(size_frame, textvariable=self.size_var,
                                      values=size_names, state="readonly", width=20)
        self.size_menu.pack(fill=tk.X, pady=(5, 0))
        self.size_menu.current(1)
        self.size_menu.bind('<<ComboboxSelected>>', self.on_size_change)

        # Custom size entry
        self.custom_frame = tk.Frame(self.settings_frame, bg=COLORS['bg_card'])
        self.custom_size_var = tk.StringVar()
        custom_label = tk.Label(self.custom_frame, text="Custom size (MB):",
                               font=('Segoe UI', 10),
                               bg=COLORS['bg_card'])
        custom_label.pack(side=tk.LEFT)
        custom_entry = ttk.Entry(self.custom_frame, textvariable=self.custom_size_var, width=10)
        custom_entry.pack(side=tk.LEFT, padx=(10, 0))

        # Quality warning
        self.warning_label = tk.Label(self.settings_frame, text="",
                                     font=('Segoe UI', 9),
                                     fg=COLORS['warning'],
                                     bg=COLORS['bg_card'])
        self.warning_label.pack(anchor=tk.W, pady=(10, 0))

        # Output format
        format_frame = tk.Frame(self.settings_frame, bg=COLORS['bg_card'])
        format_frame.pack(fill=tk.X, pady=(15, 0))

        format_label = tk.Label(format_frame, text="Output Format:",
                               font=('Segoe UI', 10, 'bold'),
                               fg=COLORS['text_primary'],
                               bg=COLORS['bg_card'])
        format_label.pack(anchor=tk.W)

        self.format_var = tk.StringVar(value="mp4")
        formats = [("MP4 (Recommended)", "mp4"),
                  ("Keep Original", "original"),
                  ("WebM", "webm"),
                  ("MOV", "mov")]

        for text, value in formats:
            rb = tk.Radiobutton(format_frame, text=text, value=value,
                               variable=self.format_var,
                               font=('Segoe UI', 9),
                               bg=COLORS['bg_card'],
                               selectcolor=COLORS['primary'])
            rb.pack(anchor=tk.W, pady=2)

        # Quality preset
        quality_frame = tk.Frame(self.settings_frame, bg=COLORS['bg_card'])
        quality_frame.pack(fill=tk.X, pady=(15, 0))

        quality_label = tk.Label(quality_frame, text="Quality Preset:",
                                font=('Segoe UI', 10, 'bold'),
                                fg=COLORS['text_primary'],
                                bg=COLORS['bg_card'])
        quality_label.pack(anchor=tk.W)

        self.quality_var = tk.StringVar(value="medium")
        qualities = [
            ("High - Best quality", "high"),
            ("Balanced - Good compression", "medium"),
            ("Compact - Smallest size", "low")
        ]

        for text, value in qualities:
            rb = tk.Radiobutton(quality_frame, text=text, value=value,
                               variable=self.quality_var,
                               font=('Segoe UI', 9),
                               bg=COLORS['bg_card'],
                               selectcolor=COLORS['primary'])
            rb.pack(anchor=tk.W, pady=2)

        # Compress button
        self.compress_btn = tk.Button(self.settings_frame, text="Compress Video",
                                     font=('Segoe UI', 12, 'bold'),
                                     bg=COLORS['primary'],
                                     fg='white',
                                     activebackground=COLORS['primary_dark'],
                                     activeforeground='white',
                                     padx=40, pady=15,
                                     cursor='hand2',
                                     relief=tk.FLAT,
                                     command=self.start_compression)
        self.compress_btn.pack(pady=(25, 0))

    def create_progress_section(self):
        """Create progress section"""
        self.progress_frame = self.create_card(self.scrollable_frame, "Compressing Video...")
        self.progress_frame.pack_forget()  # Hide initially

        # Progress percentage
        self.progress_percent = tk.Label(self.progress_frame, text="0%",
                                        font=('Segoe UI', 32, 'bold'),
                                        fg=COLORS['primary'],
                                        bg=COLORS['bg_card'])
        self.progress_percent.pack(pady=(10, 5))

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.progress_frame, length=500, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=(10, 15))

        # Status text
        self.status_label = tk.Label(self.progress_frame, text="Initializing...",
                                    font=('Segoe UI', 10),
                                    fg=COLORS['text_secondary'],
                                    bg=COLORS['bg_card'])
        self.status_label.pack()

        # Cancel button
        self.cancel_btn = tk.Button(self.progress_frame, text="Cancel",
                                   font=('Segoe UI', 10),
                                   bg=COLORS['border'],
                                   fg=COLORS['text_primary'],
                                   activebackground=COLORS['text_muted'],
                                   padx=20, pady=8,
                                   cursor='hand2',
                                   relief=tk.FLAT,
                                   command=self.cancel_compression)
        self.cancel_btn.pack(pady=(20, 0))

    def create_result_section(self):
        """Create results section (called after compression)"""
        if hasattr(self, 'result_frame'):
            self.result_frame.destroy()

        self.result_frame = self.create_card(self.scrollable_frame, "Compression Complete!")

        # Comparison
        comparison_frame = tk.Frame(self.result_frame, bg=COLORS['bg_card'])
        comparison_frame.pack(fill=tk.X, pady=20)

        # Before
        before_frame = tk.Frame(comparison_frame, bg=COLORS['bg_light'], padx=20, pady=15)
        before_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=(0, 10))

        tk.Label(before_frame, text="Original Size",
                font=('Segoe UI', 9),
                fg=COLORS['text_muted'],
                bg=COLORS['bg_light']).pack()
        tk.Label(before_frame, text=self.format_size(self.video_info['size']),
                font=('Segoe UI', 16, 'bold'),
                fg=COLORS['text_primary'],
                bg=COLORS['bg_light']).pack()

        # Arrow
        arrow_label = tk.Label(comparison_frame, text="➜",
                              font=('Segoe UI', 24),
                              fg=COLORS['primary'],
                              bg=COLORS['bg_card'])
        arrow_label.pack(side=tk.LEFT, padx=10)

        # After
        after_frame = tk.Frame(comparison_frame, bg=COLORS['bg_light'], padx=20, pady=15)
        after_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=(10, 0))

        tk.Label(after_frame, text="Compressed Size",
                font=('Segoe UI', 9),
                fg=COLORS['text_muted'],
                bg=COLORS['bg_light']).pack()
        self.compressed_size_label = tk.Label(after_frame, text="-",
                                             font=('Segoe UI', 16, 'bold'),
                                             fg=COLORS['success'],
                                             bg=COLORS['bg_light'])
        self.compressed_size_label.pack()

        # Savings badge
        self.savings_label = tk.Label(self.result_frame, text="",
                                     font=('Segoe UI', 14, 'bold'),
                                     fg=COLORS['success'],
                                     bg=COLORS['bg_card'])
        self.savings_label.pack(pady=15)

        # Output path
        self.output_path_label = tk.Label(self.result_frame, text="",
                                         font=('Segoe UI', 9),
                                         fg=COLORS['text_muted'],
                                         bg=COLORS['bg_card'],
                                         wraplength=600)
        self.output_path_label.pack(pady=(0, 15))

        # Buttons
        btn_frame = tk.Frame(self.result_frame, bg=COLORS['bg_card'])
        btn_frame.pack(pady=(10, 0))

        self.open_folder_btn = tk.Button(btn_frame, text="Open Folder",
                                        font=('Segoe UI', 10, 'bold'),
                                        bg=COLORS['primary'],
                                        fg='white',
                                        activebackground=COLORS['primary_dark'],
                                        padx=25, pady=10,
                                        cursor='hand2',
                                        relief=tk.FLAT,
                                        command=self.open_output_folder)
        self.open_folder_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.new_video_btn = tk.Button(btn_frame, text="Compress Another",
                                      font=('Segoe UI', 10),
                                      bg=COLORS['border'],
                                      fg=COLORS['text_primary'],
                                      activebackground=COLORS['text_muted'],
                                      padx=25, pady=10,
                                      cursor='hand2',
                                      relief=tk.FLAT,
                                      command=self.reset)
        self.new_video_btn.pack(side=tk.LEFT, padx=(10, 0))

        # Scroll to result
        self.result_frame.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def find_ffmpeg(self):
        """Find FFmpeg executable"""
        # Check if ffmpeg is in PATH
        try:
            result = subprocess.run(['ffmpeg', '-version'],
                                capture_output=True,
                                text=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
            if result.returncode == 0:
                return 'ffmpeg'
        except FileNotFoundError:
            pass

        # Check common locations on Windows
        if sys.platform == 'win32':
            common_paths = [
                r'C:\ffmpeg\bin\ffmpeg.exe',
                r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
                r'C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe',
                os.path.join(os.path.dirname(sys.executable), 'ffmpeg.exe'),
            ]
            for path in common_paths:
                if os.path.exists(path):
                    return path

        return None

    def show_ffmpeg_error(self):
        """Show FFmpeg not found error"""
        messagebox.showerror(
            "FFmpeg Not Found",
            "FFmpeg is required but not found.\n\n"
            "Please install FFmpeg:\n"
            "1. Download from https://ffmpeg.org/download.html\n"
            "2. Extract to C:\\ffmpeg\n"
            "3. Add C:\\ffmpeg\\bin to your PATH\n\n"
            "Or place ffmpeg.exe in the same folder as this app."
        )

    def select_file(self):
        """Open file dialog to select video"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video files", "*.mp4 *.mov *.avi *.mkv *.webm *.flv *.wmv"),
                ("MP4 files", "*.mp4"),
                ("MOV files", "*.mov"),
                ("AVI files", "*.avi"),
                ("MKV files", "*.mkv"),
                ("WebM files", "*.webm"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        # Check file size (10GB limit)
        size = os.path.getsize(file_path)
        if size > 10 * 1024 * 1024 * 1024:
            messagebox.showerror("Error", "File size exceeds 10GB limit")
            return

        self.current_file = file_path
        self.file_label.config(text=f"Selected: {os.path.basename(file_path)}")

        # Get video info
        self.get_video_info(file_path)

    def get_video_info(self, file_path):
        """Get video metadata using FFmpeg"""
        if not self.ffmpeg_path:
            return

        try:
            # Run ffprobe if available, otherwise use ffmpeg
            cmd = [self.ffmpeg_path.replace('ffmpeg', 'ffprobe') if 'ffprobe' in self.ffmpeg_path else self.ffmpeg_path,
                   '-v', 'error',
                   '-select_streams', 'v:0',
                   '-show_entries', 'stream=width,height,duration',
                   '-show_entries', 'format=duration',
                   '-of', 'json',
                   file_path]

            # Use ffprobe if available
            ffprobe_path = self.ffmpeg_path.replace('ffmpeg', 'ffprobe')
            if os.path.exists(ffprobe_path):
                cmd[0] = ffprobe_path
            else:
                # Fallback: estimate from file
                cmd = [self.ffmpeg_path, '-i', file_path]

            result = subprocess.run(cmd, capture_output=True, text=True,
                                  creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)

            # Parse duration from output
            duration = 0
            width, height = 1920, 1080

            try:
                if 'ffprobe' in cmd[0]:
                    data = json.loads(result.stdout)
                    if 'streams' in data and data['streams']:
                        stream = data['streams'][0]
                        width = int(stream.get('width', 1920))
                        height = int(stream.get('height', 1080))
                        duration = float(stream.get('duration', 0))
                    if 'format' in data and data['format']:
                        duration = float(data['format'].get('duration', duration))
                else:
                    # Parse from ffmpeg output
                    import re
                    match = re.search(r'Duration: (\d+):(\d+):(\d+)', result.stderr)
                    if match:
                        hours, mins, secs = map(int, match.groups())
                        duration = hours * 3600 + mins * 60 + secs
            except:
                pass

            self.video_info = {
                'path': file_path,
                'name': os.path.basename(file_path),
                'size': size,
                'duration': duration,
                'width': width,
                'height': height,
                'format': os.path.splitext(file_path)[1].upper().replace('.', '')
            }

            self.update_info_display()
            self.generate_recommendations()
            self.show_settings()

        except Exception as e:
            messagebox.showerror("Error", f"Could not read video info: {str(e)}")

    def update_info_display(self):
        """Update video info display"""
        if not self.video_info:
            return

        self.info_labels['file_name'].config(text=self.video_info['name'])
        self.info_labels['size'].config(text=self.format_size(self.video_info['size']))
        self.info_labels['duration'].config(text=self.format_duration(self.video_info['duration']))
        self.info_labels['format'].config(text=self.video_info['format'])
        self.info_labels['resolution'].config(text=f"{self.video_info['width']}x{self.video_info['height']}")

        self.info_frame.master.pack(fill=tk.X, pady=(0, 15), padx=5)

    def show_settings(self):
        """Show settings section"""
        self.settings_frame.master.pack(fill=tk.X, pady=(0, 15), padx=5)
        self.scrollable_frame.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def format_size(self, bytes_val):
        """Format bytes to human readable"""
        if bytes_val == 0:
            return "0 B"
        k = 1024
        sizes = ['B', 'KB', 'MB', 'GB']
        i = int(bytes_val // k ** len(sizes))
        if i >= len(sizes):
            i = len(sizes) - 1
        size = bytes_val / (k ** i)
        return f"{size:.2f} {sizes[i]}"

    def format_duration(self, seconds):
        """Format seconds to duration string"""
        if not seconds:
            return "Unknown"
        mins = int(seconds // 60)
        secs = int(seconds % 60)
        if mins > 0:
            return f"{mins}:{secs:02d}"
        return f"{secs}s"

    def generate_recommendations(self):
        """Generate size recommendations"""
        if not self.video_info:
            return

        size_mb = self.video_info['size'] / (1024 * 1024)

        # Clear previous
        for widget in self.rec_frame.winfo_children():
            widget.destroy()

        recommendations = []
        if size_mb < 100:
            recommendations = [
                (int(size_mb * 0.5), "Best Quality", COLORS['success']),
                (int(size_mb * 0.25), "Compact", COLORS['warning'])
            ]
        elif size_mb < 500:
            recommendations = [
                (100, "Best Quality", COLORS['success']),
                (250, "Good Compression", COLORS['primary']),
                (int(size_mb * 0.5), "Half Size", COLORS['warning'])
            ]
        elif size_mb < 2000:
            recommendations = [
                (500, "Best Quality", COLORS['success']),
                (1000, "Good Compression", COLORS['primary']),
                (int(size_mb * 0.4), "Compact", COLORS['warning'])
            ]
        else:
            recommendations = [
                (1000, "Best Quality", COLORS['success']),
                (2000, "Good Compression", COLORS['primary']),
                (5000, "Maximum Compression", COLORS['warning'])
            ]

        # Filter valid recommendations
        recommendations = [r for r in recommendations if r[0] < size_mb]

        for size, label, color in recommendations:
            btn = tk.Button(self.rec_frame, text=f"{label}\n{size} MB",
                          font=('Segoe UI', 9),
                          bg=color,
                          fg='white',
                          activebackground=color,
                          padx=15, pady=8,
                          cursor='hand2',
                          relief=tk.FLAT,
                          command=lambda s=size: self.set_custom_size(s))
            btn.pack(side=tk.LEFT, padx=(0, 10))

    def set_custom_size(self, size_mb):
        """Set custom size from recommendation"""
        self.size_var.set("custom")
        self.custom_size_var.set(str(size_mb))
        self.on_size_change(None)

    def on_size_change(self, event):
        """Handle size selection change"""
        if self.size_var.get() == "custom":
            self.custom_frame.pack(fill=tk.X, pady=(10, 0), before=self.warning_label)
        else:
            self.custom_frame.pack_forget()

        self.check_quality_impact()

    def check_quality_impact(self):
        """Check if compression will affect quality"""
        if not self.video_info:
            return

        size_mb = self.video_info['size'] / (1024 * 1024)

        if self.size_var.get() == "custom":
            try:
                target = float(self.custom_size_var.get())
            except:
                return
        else:
            try:
                target = float(self.size_var.get())
            except:
                return

        ratio = target / size_mb

        if ratio >= 0.7:
            self.warning_label.config(text="")
        elif ratio >= 0.5:
            self.warning_label.config(text="⚠ Slight quality reduction may be noticeable")
        elif ratio >= 0.3:
            self.warning_label.config(text="⚠ Noticeable quality reduction expected")
        else:
            self.warning_label.config(text="⚠ Significant quality reduction expected")

    def start_compression(self):
        """Start video compression"""
        if not self.current_file or not self.ffmpeg_path:
            return

        # Get target size
        if self.size_var.get() == "custom":
            try:
                target_mb = float(self.custom_size_var.get())
            except:
                messagebox.showerror("Error", "Please enter a valid custom size")
                return
        else:
            try:
                target_mb = float(self.size_var.get())
            except:
                messagebox.showerror("Error", "Please select a target size")
                return

        size_mb = self.video_info['size'] / (1024 * 1024)
        if target_mb >= size_mb:
            messagebox.showerror("Error", "Target size must be smaller than original")
            return

        # Generate output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.dirname(self.current_file)
        base_name = os.path.splitext(self.video_info['name'])[0]

        output_format = self.format_var.get()
        if output_format == "original":
            output_format = self.video_info['format'].lower()

        self.output_path = os.path.join(output_dir, f"{base_name}_compressed_{timestamp}.{output_format}")

        # Show progress
        self.settings_frame.master.pack_forget()
        self.progress_frame.master.pack(fill=tk.X, pady=(0, 15), padx=5)
        self.compression_running = True
        self.cancelled = False

        # Start compression in thread
        thread = threading.Thread(target=self.compress_video,
                                 args=(target_mb, self.output_path))
        thread.daemon = True
        thread.start()

    def compress_video(self, target_mb, output_path):
        """Compress video using FFmpeg"""
        try:
            duration = self.video_info['duration'] if self.video_info['duration'] > 0 else 300

            # Calculate bitrate
            target_bits = target_mb * 8 * 1024 * 1024
            total_bitrate = int(target_bits / duration)
            video_bitrate = int(total_bitrate * 0.95)
            audio_bitrate = min(128000, int(total_bitrate * 0.05))

            # Quality CRF
            quality = self.quality_var.get()
            crf = {'high': 18, 'medium': 23, 'low': 28}.get(quality, 23)

            # Build FFmpeg command
            cmd = [
                self.ffmpeg_path,
                '-i', self.current_file,
                '-c:v', 'libx264',
                '-preset', 'medium',
                '-crf', str(crf),
                '-b:v', str(video_bitrate),
                '-maxrate', str(video_bitrate),
                '-bufsize', str(video_bitrate * 2),
                '-c:a', 'aac',
                '-b:a', str(audio_bitrate),
                '-movflags', '+faststart',
                '-y',
                output_path
            ]

            # Run with progress
            self.update_status("Starting compression...")

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )

            # Monitor progress
            while True:
                if self.cancelled:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except:
                        process.kill()
                    if os.path.exists(output_path):
                        os.remove(output_path)
                    return

                ret = process.poll()
                if ret is not None:
                    break

                self.root.after(100, lambda: None)

            if process.returncode == 0 and os.path.exists(output_path):
                self.compression_complete(output_path)
            else:
                stderr = process.stderr.read() if process.stderr else "Unknown error"
                self.compression_failed(stderr)

        except Exception as e:
            self.compression_failed(str(e))

    def update_status(self, text):
        """Update status label"""
        self.root.after(0, lambda: self.status_label.config(text=text))

    def update_progress(self, value):
        """Update progress"""
        self.root.after(0, lambda: [
            self.progress_bar.config(value=value),
            self.progress_percent.config(text=f"{int(value)}%")
        ])

    def compression_complete(self, output_path):
        """Handle successful compression"""
        self.compression_running = False
        self.compressed_file = output_path

        output_size = os.path.getsize(output_path)
        savings = (1 - output_size / self.video_info['size']) * 100

        self.root.after(0, lambda: [
            self.progress_frame.master.pack_forget(),
            self.create_result_section(),
            self.compressed_size_label.config(text=self.format_size(output_size)),
            self.savings_label.config(text=f"🎉 {savings:.1f}% size reduction!"),
            self.output_path_label.config(text=f"Saved to: {output_path}")
        ])

    def compression_failed(self, error):
        """Handle compression failure"""
        self.compression_running = False
        self.root.after(0, lambda: [
            self.progress_frame.master.pack_forget(),
            self.settings_frame.master.pack(fill=tk.X, pady=(0, 15), padx=5),
            messagebox.showerror("Compression Failed", f"Error: {error}")
        ])

    def cancel_compression(self):
        """Cancel ongoing compression"""
        if self.compression_running:
            self.cancelled = True
            self.update_status("Cancelling...")

    def open_output_folder(self):
        """Open output folder in file explorer"""
        if hasattr(self, 'output_path') and self.output_path:
            folder = os.path.dirname(self.output_path)
            os.startfile(folder) if sys.platform == 'win32' else os.system(f'open "{folder}"')

    def reset(self):
        """Reset for new video"""
        # Hide result
        if hasattr(self, 'result_frame'):
            self.result_frame.destroy()
            delattr(self, 'result_frame')

        # Hide settings and info
        self.settings_frame.master.pack_forget()
        self.info_frame.master.pack_forget()

        # Reset variables
        self.current_file = None
        self.video_info = None
        self.file_label.config(text="")
        self.size_var.set("100")
        self.custom_size_var.set("")
        self.warning_label.config(text="")

        # Scroll to top
        self.canvas.yview_moveto(0)


def main():
    """Main entry point"""
    root = tk.Tk()

    # Set DPI awareness on Windows
    if sys.platform == 'win32':
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

    app = CompressVideoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
