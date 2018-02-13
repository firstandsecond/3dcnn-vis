def html(layer_indices, number_of_filters, n_filters_per_row):
    """
    Generate html of specific structure for visualising gifs
    :param layer_indices: list of indices of convolution layers
    :param number_of_filters: number of filters for each convolution layer
    :param n_filters_per_row: number of gif images per row
    :return: Content of html file for visualising gifs
    """
    n = len(layer_indices)
    result = """<!DOCTYPE html>\n'
    <html>\n
    <head>\n\t<title>3D CNN</title>\n</head>\n
    <html>\n
    <body>\n
    \t<center>\n\t\t<h1>3D CNN Filters</h1>\n\t</center>\n
    \t<table border="5" bordercolor="blue" align="center">\n"""
    count = 0
    for l in range(n):
        result += '\t\t<tr>\n'
        result += '\t\t\t<th colspan="' + str(n_filters_per_row)+'">' + ' layer ' + str(layer_indices[l]) + '</th>\n'
        result += '\t\t</tr>\n'
        result += '\t\t<tr>\n'
        for f in range(number_of_filters[l]):
            count += 1
            result += '\t\t\t<td><img src="layer' + str(layer_indices[l]) + '/layer' + str(layer_indices[l]) + '_filter' + str(f) + '.gif" alt="" border=3 height=100 width=100></img></td>\n'
            if count%n_filters_per_row==0:
                result += '\t\t</tr>\n'
                if f != number_of_filters[l] - 1:
                    result += '\t\t<tr>\n'
    result += '</body>\n'
    result += '</html>'
    return result