# Zbar proof of concept

After cloning this repository, in the zbar directory, build the base zbar docker image.


```cd zbar && docker build -t ubuntu:zbar .```

Then build the gui docker image

```cd ../gui && docker build -t ubuntu:zbargui```

You can now run it

```docker run -d -p 5000:5000 ubuntu:zbargui```

If you want to iterate on the code and not build/restart each time, you can pass in the directory where you code is to the running container.

```docker run -d -p 5000:5000 -v /full/path/to/gui/:/app ubuntu:zbargui```

To send images from your desktop and get back a json response, use curl:

```curl -F "file=@/path/to/image.JPG" localhost:5000/scan```
