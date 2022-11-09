import matplotlib.pyplot as plt
from io import BytesIO
import base64


def get_image():
    
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as is 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the momory of the buffer
    buffer.close()

    return graph


    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as is 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the momory of the buffer
    buffer.close()

    return graph
