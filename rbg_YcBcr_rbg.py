def rgb_to_ycbcr_jpg(img_input):
    output = Variable(torch.zeros(img_input.shape))
    output[:, 0, :, :] = img_input[:, 0, :, :] * 0.299 + img_input[:, 1, :, :] * 0.587 + img_input[:, 2, :, :] * 0.114 + 0
    output[:, 1, :, :] = img_input[:, 0, :, :] * -0.168736 + img_input[:, 1, :, :] * -0.331264 + img_input[:, 2, :, :] * 0.5 + 128
    output[:, 2, :, :] = img_input[:, 0, :, :] * 0.5 + img_input[:, 1, :, :] * -0.418688 + img_input[:, 2, :, :] * -0.081312 + 128
    return output

def ycbcr_to_rgb_jpg(img_input):
    output = Variable(torch.zeros(img_input.shape))
    output[:, 0, :, :] = (img_input[:, 0, :, :]+ 0) * 1. + (img_input[:, 1, :, :]+ 0) * 0. + (img_input[:, 2, :, :]+ 0) * 1.402 
    output[:, 1, :, :] = (img_input[:, 0, :, :]- 128) * 1. + (img_input[:, 1, :, :]- 128) * -0.344136 + (img_input[:, 2, :, :]- 128) * -0.714136 
    output[:, 2, :, :] = (img_input[:, 0, :, :]- 128) * 1. + (img_input[:, 1, :, :]- 128) * 1.772 + (img_input[:, 2, :, :]- 128) * 0.
    return output