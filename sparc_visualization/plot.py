from sparc_visualization.plots.plot import get_plot_class
from sparc_visualization.objects.board import get_board_from_data
from sparc_visualization.util import encode_image_to_base64


def get_puzzle_image(
        puzzle,
        plot_type="original",
        base_64_image=False,
        show_plot=False,
        save_to_disk=False,
        save_dir=".",
        save_filename="puzzle_image.png",
):
    """Render a SPaRC puzzle and return it as a PIL image (or base64).

    Parameters
    ----------
    puzzle:
        The puzzle data of a single SPaRC puzzle.
    plot_type:
        - "original" (default)
        - "start_end_marked"
        - "coordinate_grid"
        - "coordinate_grid_and_start_end_marked"
        - "path_cell_annotated"
        - "text"
        - "low_contrast"
        - "low_contrast_and_path_cell_annotated"
        - "low_resolution"
        - "low_resolution_and_path_cell_annotated"
        - "rotated"
        - "rotated_and_path_cell_annotated"
        - "black_frame"
        - "black_frame_and_path_cell_annotated"
    base_64_image:
        If True, returns a base64-encoded string instead of a PIL Image.
    show_plot:
        If True, shows the plot in a GUI window.
    save_to_disk:
        If True, saves the plot to disk.
    save_dir:
        Directory to save the plot if ``save_to_disk=True``.
    save_filename:
        Filename to save the plot if ``save_to_disk=True``.

    Returns
    -------
    PIL.Image.Image | str
        Either a PIL Image (default) or a base64-encoded string if ``base_64_image=True``.
    """
    board = get_board_from_data(puzzle)
    plot = get_plot_class(plot_type, board, size=(board.width, board.height))
    plot.render()
    if save_to_disk:
        plot.save(dir=save_dir, filename=save_filename)
    if show_plot:
        plot.show()
    if base_64_image:
        return encode_image_to_base64(plot._img)
    else:
        return plot._img

