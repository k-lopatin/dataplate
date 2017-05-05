#!/bin/bash

sudo chmod +x *.sh

sudo apt-get install nodejs
sudo apt-get install npm

npm init

npm install --save react
npm install --save react-dom

npm install --save-dev webpack
npm install --save-dev babel-loader babel-core
npm install --save-dev babel-preset-es2015
npm install --save-dev babel-preset-react
npm install --save-dev react-d3-components

echo '{ "presets": ["react","es2015"] }' > .babelrc

