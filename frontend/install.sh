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
npm install --save react-d3-components
npm install --save recharts
sudo npm install webpack-dev-server -g
npm install webpack-dev-server --save-dev
npm install --save jquery
npm install --save-dev jquery

echo '{ "presets": ["react","es2015"] }' > .babelrc

