const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");
const isDev = !process.env.NODE_ENV || process.env.NODE_ENV === "development";

module.exports = {
    mode: isDev ? "development" : "production",
    entry: {
        script: path.resolve(__dirname, "src/index.js"),
    },
    devServer: {
        port: 5005,
    },
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "[name].js",
    },
    plugins: [
        new CopyPlugin({
            patterns: [{ from: "public", to: "./" }],
        }),
    ],
};
