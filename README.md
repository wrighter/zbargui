# Zbar proof of concept

After cloning this repository, in the zbar directory, build the base zbar docker image.


```cd zbar && docker build -t ubuntu:zbar .```

Then build the gui docker image

```cd ../gui && docker build -t ubuntu:zbargui```

You can now run it

```docker run -d -p 5000:5000 ubuntu:zbargui```


