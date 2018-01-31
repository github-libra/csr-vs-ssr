const webpack = require('webpack')
const CompressionWebpackPlugin = require('compression-webpack-plugin')

module.exports = {
  entry: {
    app: ['./index.js']
  },
  output: {
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      },
    ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin(),
    new CompressionWebpackPlugin({
      asset: '[path].gz[query]',
      algorithm: 'gzip',
      test: new RegExp(
        '\\.(' +
        ['js'].join('|') +
        ')$'
      ),
      threshold: 10240,
      minRatio: 0.8
    })
  ]
}