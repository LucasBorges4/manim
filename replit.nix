{pkgs}: {
  deps = [
    pkgs.texliveFull
    pkgs.texliveMedium
    pkgs.texliveSmall
    pkgs.harfbuzz
    pkgs.pangomm
    pkgs.cairomm
    pkgs.ghostscript
    pkgs.ffmpeg
    pkgs.pkg-config
    pkgs.pango
    pkgs.cairo
  ];
}
