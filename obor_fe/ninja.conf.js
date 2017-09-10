module.exports = {
    template: "swig", // whatever template engine you like
    mock: "/mock/mock.json", // dir for mock data
    webpack: true, // flag for using webpack or not
    proxy: {
        route: "/api",
        origin: "http://120.24.4.254:8822/"
    },
    // proxy: {
    // 	route: "/api",
    // 	origin: "http://xueer.muxixyz.com"
    // },
    staticDir: "/static",
    templateDir: "/templates",
}