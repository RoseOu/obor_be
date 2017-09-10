const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const autoprefixer = require('autoprefixer');

module.exports = {
    entry: {
        'main.js': ['./src/main.js'],
        'manage.js': ['./src/manage.js'],
        'login.js': ['./src/login.js'],
        'learn.js': ['./src/learn.js'],
        'about.js': ['./src/about.js']
    },
    output: {
        path: path.join(__dirname, ""),
        publicPath: '/dist/',
        filename: '[name]'
    },
    module: {
        loaders: [{
                test: /\.vue$/,
                loader: 'vue',
                options: {
                    cssModules: {
                        localIdentName: '[name]-[local]-[hash:base64:5]',
                        camelCase: true
                    }
                }
            }, {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            }, {
                test: /\.(html|tpl)$/,
                loader: 'html-loader'
            }, {
                test: /\.(png|jpg|gif|svg|jpeg)$/i,
                loader: 'url-loader?limit=20&name=[hash:8].[name].[ext]'
            }, {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /\.scss$/,
                loaders: ["style", "css", "sass"]
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
                loader: 'file-loader'
            }
        ]
    },
    devtool: '#eval-source-map',
    resolve: {
        extensions: ['', '.js', '.scss', '.vue'],
    },
    plugins: [
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(),
        // new HtmlWebpackPlugin({
        //     filename: 'templates/home.html',
        //     template: './templates/home.ejs',
        //     inject: false
        // }),
        // new HtmlWebpackPlugin({
        //     filename: 'templates/editor.html',
        //     template: './templates/editor.ejs',
        //     inject: false
        // })
    ]
};