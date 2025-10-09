def contrast_stretch(img, r_min, r_max):
    # Linear contrast stretching
    vmax = 0
    vmin = 255
    stretched_img = (img - r_min) * ((vmax - vmin) / (r_max - r_min)) + vmin
    return stretched_img
