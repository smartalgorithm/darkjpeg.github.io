darkjpeg
========

DarkJPEG is a new generation open source steganography web service. It is supposed to serve people's needs for the freedom of communication even in those countries which break human rights by forcing some kind of Internet censorship or even denying to use cryptography by law. The service uses strong steganography methods to hide the very fact of hiding data among with strong cryptography methods to protect the data of being read by non-trusted groups of people.

Main features:
- SHA3 key generation;
- AES256 encryption;
- JPEG steganography;
- Random containers;
- Client side encoding;
- Anonymity and privacy;
- MIT License.

Supported encapsulation methods:
- auto, which is used by default and suitable for most cases (note: data is being encoded with the join method);
- join, which simply concatenates a container and encrypted data together producing a valid JPEG on the output and giving infinite container capacity among with moderate security;
- steg, which uses strong steganography algorithms allowing to inject encrypted data directly into JPEG discrete cosine transform coefficients and giving about 20% of the container size capacity and the maximal security level, please note this is the only method to be used in the case of hiding some serious content.

Supported container types:
- rand, which downloads a random image from Wikimedia;
- grad, which generates a random image using gradient algorithms;
- image, which allows to use one's own image as a container.

### RarJPEG support

It was decided not to allow one to use an empty password for the security reasons. However, this could be done using the join method producing a concatenation of two files together. This gives an ability to join e.g. a rar-archive to any JPEG container which then could be simply opened by any archive software without any need in this service. Note: every encoded file has an additional header in the beginning and JPEG EOI (0xFFD9) word at the end in the reasons of security.

### Server-less

No server is needed to encode or decode files at all. All computations are being run on the client giving additional performance and privacy, so the service never tracks any requests, therefore nobody could possibly know about one's actions what gives one maximum anonymity and security.

### HUGS support

This service allows to provide a URL instead of selecting or drag'n'dropping a file. But note that there is a web-restriction named CORS which denies the service to download data directly from other domains. So there are two proxy services (hugs-01 and hugs-02) running on the Google App Engine platform. They are an optional part allowing not to download files manually but with the HUGS support. Note: there's a daily bandwidth quota of 2048 MiB had been set by Google and since the service out of it, a URL cannot be used instead of a file. In that case please mention there is a special browser extension available which gives an ability to decode images directly on any website just by clicking a context menu item on it.

### Developer's guide

The service core is built as an asynchronous web-worker dark.js. It can deal with the following json-requests:
- {action: 'encrypt', name: 'filename.ext', pass: 'password', buffer: ArrayBuffer}
- {action: 'encode', method: 'auto|join|steg', width: ImageData.width, height: ImageData.height, buffer: ImageData}
- {action: 'decode', method: 'auto|join|steg', buffer: ArrayBuffer}
- {action: 'decrypt', pass: 'password'}

The answers should be processed by the worker.onmessage function and look like this:
- {type: 'encrypt', size: encrypted}
- {type: 'encode', time: duration, isize: result.length, csize: encoded.length, rate: 100*isize/csize, buffer: ArrayBuffer}
- {type: 'decode', time: duration, isize: result.length, csize: decoded.length, rate: 100*isize/csize}
- {type: 'decrypt', name: 'filename.ext', buffer: ArrayBuffer}
- {type: 'progress', name: 'encrypt|decrypt|encode|decode', progress: percent}
- {type: 'error', name: 'encrypt|decrypt|encode|decode', msg: message}

### Thanks to

- Emily Stark, Mike Hamburg, Dan Boneh, Stanford University for their BSD-licensed JavaScript AES256 implementation;
- Chris Drost for his public domain implementation of SHA3 Keccak;
- Yury Delendik, Brendan Dahl, notmasteryet for their Apache licensed JavaScript JPEG decoder;
- Andreas Ritter for his amazing Apache licensed JavaScript JPEG encoder port;
- Dan Gries for his examples of very pretty fractal linear gradients drawings;
- Brsev for the gear icon (a part of his CC BY-NC-ND licensed Token Dark icon pack);
- Anoxia-Photography for the Limbo photo used as a background.

### License

Copyright © 2013 Mikhail Mukovnikov &lt;m.mukovnikov@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
