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

function show_image(element, file) {
    const reader = new FileReader();
    reader.onload = () => { element.src = reader.result; }
    reader.readAsDataURL(file);
}

function add_class(element, cls) {
    element.classList.add(cls);
}

function remove_class(element, cls) {
    element.classList.remove(cls);
}

function find_parent_by_class(element, cls) {
    let buf = element.parentNode;
    while (!buf.classList.contains(cls)) buf = buf.parentNode;
    return buf;
}

function post_employee_data(form, event, url) {
    // stop defalt submit process
    event.stopPropagation();
    event.preventDefault();

    // show processing text
    const submit_btn = form.querySelector('.submit-button');
    const submit_btn_textcontent = submit_btn.textContent;
    submit_btn.textContent = '保存中';
    submit_btn.disabled = true;

    fetch(url, {
      method: 'POST',
      body: new FormData(form),
    })
    .then(res => {
      if (res.ok) location.reload();
    })
    .finally(() => {
      submit_btn.textContent = submit_btn_textcontent;
      submit_btn.disabled = false;
    });
}