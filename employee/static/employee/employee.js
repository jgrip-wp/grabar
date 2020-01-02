function make_url(url, params) {
    if (params != null && Object.keys(params).length > 0) {
        url = url + '?' + Object.entries(params).map(x => x.map(encodeURIComponent).join('=')).join('&');
    }
    return url;
}

function get_component_values(selector) {
    const values = {};
    for (let c of document.querySelectorAll(selector)) {
        values[c.name] = c.value;
    }
    return values;
}
