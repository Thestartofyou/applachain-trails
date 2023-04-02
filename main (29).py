import requests
import folium

# Define the coordinates for the start and end points of the trail
start = (34.7298, -84.8635)
end = (38.5395, -78.0405)

# Define a list of GPS coordinates for the Appalachian Trail
appalachian_trail = [(34.7298, -84.8635), (34.7413, -84.8302), (34.7505, -84.7895), (34.7679, -84.7291), (34.7762, -84.6708), (34.7911, -84.6201), (34.8021, -84.5975), (34.8098, -84.5702), (34.8281, -84.5209), (34.8424, -84.4591), (34.8646, -84.4064), (34.8769, -84.3571), (34.8906, -84.3192), (34.9086, -84.2906), (34.9231, -84.2593), (34.9417, -84.2228), (34.9544, -84.1984), (34.9659, -84.1698), (34.9796, -84.1398), (34.9945, -84.1033), (35.0071, -84.0773), (35.0208, -84.053), (35.0378, -84.0165), (35.053, -83.9878), (35.0652, -83.9464), (35.0852, -83.9151), (35.1049, -83.8772), (35.121, -83.8458), (35.1385, -83.8145), (35.1585, -83.7815), (35.1745, -83.7515), (35.1936, -83.7271), (35.2146, -83.6985), (35.2368, -83.6669), (35.2566, -83.6376), (35.2746, -83.6093), (35.2934, -83.5735), (35.317, -83.5458), (35.3414, -83.5171), (35.3579, -83.4979), (35.3744, -83.476), (35.3927, -83.4409), (35.4149, -83.4152), (35.4327, -83.3866), (35.4544, -83.3579), (35.4787, -83.3266), (35.4984, -83.3016), (35.5179, -83.2743), (35.5381, -83.2443), (35.5592, -83.2142), (35.578, -83.1876), (35.5936, -83.1546), (35.6181, -83.1269)]

# Create a map object and center it on the starting point of the trail
map = folium.Map(location=start, zoom_start=8)

# Add markers for the Appalachian

