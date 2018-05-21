# 3dcnn-vis

Visualizing activations of 3D convolutional filters using keras-vis library.

## Model architecture

|Layer (type)         |        Output Shape         |     Param |   
|---|---|---|
|conv1 (Conv3D)       |        (None, 16, 112, 112, 64) | 5248  |    
|pool1 (MaxPooling3D) |        (None, 16, 56, 56, 64)   | 0     |   
|conv2 (Conv3D)       |        (None, 16, 56, 56, 128)  | 221312|
|pool2 (MaxPooling3D) |        (None, 8, 28, 28, 128)   | 0     |    
conv3a (Conv3D)       |       (None, 8, 28, 28, 256)    |884992 |   
conv3b (Conv3D)       |       (None, 8, 28, 28, 256)    |1769728|   
pool3 (MaxPooling3D)  |       (None, 4, 14, 14, 256)    |0      |   
conv4a (Conv3D)       |       (None, 4, 14, 14, 512)    |3539456|   
conv4b (Conv3D)       |       (None, 4, 14, 14, 512)    |7078400|   
pool4 (MaxPooling3D)  |       (None, 2, 7, 7, 512)      |0      |   
conv5a (Conv3D)       |       (None, 2, 7, 7, 512)      |7078400|   
conv5b (Conv3D)       |       (None, 2, 7, 7, 512)      |7078400|   
zero_padding3d_2 (ZeroPadding)| (None, 2, 9, 9, 512)    |  0    |     
pool5 (MaxPooling3D)  |       (None, 1, 4, 4, 512)      |0      |   
flatten_2 (Flatten)   |       (None, 8192)              |0      |   
fc6 (Dense)           |       (None, 4096)              |33558528|  
dropout_3 (Dropout)   |       (None, 4096)              |0       |  
fc7 (Dense)           |       (None, 4096)              |16781312|  
dropout_4 (Dropout)   |       (None, 4096)              |0       |  
fc8 (Dense)           |       (None, 487)               |1995239 |  

## Weights
Possible to [use the pre-trained model in Caffe format or convert it to Keras format](https://github.com/axon-research/c3d-keras) or simply download model weights in Keras format from [here](https://www.dropbox.com/s/vh293aba931wrk1/sports1M_weights_tf.h5?dl=0).

## 3D CNN cativations of filters

conv1
<table border="0">
		<tr>
			<td><img src="./data/layer0/layer0_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer0/layer0_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer0/layer0_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer0/layer0_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
 </table>
conv2
<table>
  <tr>
    <td><img src="./data/layer2/layer2_filter0.gif" alt="" border=3 height=100 width=100></img></td>
    <td><img src="./data/layer2/layer2_filter1.gif" alt="" border=3 height=100 width=100></img></td>
    <td><img src="./data/layer2/layer2_filter2.gif" alt="" border=3 height=100 width=100></img></td>
    <td><img src="./data/layer2/layer2_filter3.gif" alt="" border=3 height=100 width=100></img></td>
  </tr>
</table>
conv3a
<table>
		<tr>
			<td><img src="./data/layer4/layer4_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer4/layer4_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer4/layer4_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer4/layer4_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
conv3b
<table>
        <tr>
			<td><img src="./data/layer5/layer5_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer5/layer5_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer5/layer5_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer5/layer5_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
conv4a
<table>
		<tr>
			<td><img src="./data/layer7/layer7_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer7/layer7_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer7/layer7_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer7/layer7_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
conv4b
<table>
        <tr>
			<td><img src="./data/layer8/layer8_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer8/layer8_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer8/layer8_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer8/layer8_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
conv5a
<table>
    	<tr>
			<td><img src="./data/layer10/layer10_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer10/layer10_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer10/layer10_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer10/layer10_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
conv5b
<table>
    	<tr>
			<td><img src="./data/layer11/layer11_filter0.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer11/layer11_filter1.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer11/layer11_filter2.gif" alt="" border=3 height=100 width=100></img></td>
			<td><img src="./data/layer11/layer11_filter3.gif" alt="" border=3 height=100 width=100></img></td>
		</tr>
</table>
