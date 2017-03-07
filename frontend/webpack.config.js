module.exports={
    context: __dirname + "/ES6/lib",
    entry: "./app.jsx",
    output: {
        path: __dirname + "/ES6/dist",
        filename: "bundle.js"
    },
    module: {
        loaders: [

            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                loader: ['babel'],
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    }
};