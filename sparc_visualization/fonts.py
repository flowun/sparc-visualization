from typing import Optional

from PIL import ImageFont


def load_plot_font(size: int, preferred_path: Optional[str] = None):
    """Load a truetype font with robust fallbacks for cluster/headless environments."""
    candidates = []

    if preferred_path:
        candidates.append(preferred_path)

    candidates.extend(
        [
            "arial.ttf",
            "DejaVuSansMono.ttf",
            "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "C:/Windows/Fonts/DejaVuSansMono.ttf",
            "C:/Windows/Fonts/arial.ttf",
        ]
    )

    for font_candidate in candidates:
        try:
            # Let Pillow resolve bare font names through platform font lookup.
            return ImageFont.truetype(font_candidate, size=size)
        except OSError:
            continue

    return ImageFont.load_default()


if __name__ == "__main__":
    # Test font loading
    font = load_plot_font(size=20)
    print("Loaded font:", font.getname())