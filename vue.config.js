module.exports = {
  publicPath: '/',
  assetsDir: 'static',
  outputDir: 'dist',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
      },
    },
  },
};
