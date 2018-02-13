import keras
from vis.visualization import get_num_filters, visualize_activation
from moviepy.editor import ImageSequenceClip

def visualize_all_activations(model, destination_path):
    """
    Get all activations of all convolutional layers for each filter
    Saving activations in destination_path as .gif files in process
    :param model: keras sequential model
    :param destination_path: path where to save gifs
    :return: all activations from all layers
    """

    # get indices of all convolutional layers
    conv_layer_indices = []
    number_of_layers = len(model.layers)
    for i in range(number_of_layers):
        if type(model.layers[i]) is keras.layers.convolutional.Conv3D:
            conv_layer_indices.append(i)

    # getting number of convolutional layers
    number_of_conv_layers = len(conv_layer_indices)

    # getting number of filters for each convolutional layer
    number_of_filters = []
    for i in conv_layer_indices:
        number_of_filters.append(get_num_filters(model.layers[i]))

    # getting activations for each convolutional layer
    all_activations = []
    for l in range(number_of_conv_layers):
        activations = []
        for f in range(number_of_filters[l]):
            # getting activation
            activation = visualize_activation(model, layer_idx=conv_layer_indices[l], filter_indices=f)
            activations.append(activation)
            # saving activation
            clip = ImageSequenceClip(list(activation), fps=10).resize(1.0)
            gif_folder = destination_path + "/" + model.layers[conv_layer_indices[l]].name + "/"
            gif_name = model.layers[conv_layer_indices[l]].name + "_" + "activation" + str(f) + ".gif"
            clip.write_gif(gif_folder + gif_name, fps=10)
        all_activations.append(activations)
    return all_activations