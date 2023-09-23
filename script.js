fetch('data2.json')
    .then(response => response.json())
    .then(data => {
        const selectElement = document.getElementById('faculty');  
        selectElement.innerHTML = '<option value="default">-- Seçiniz --</option>';
        const keys = Object.keys(data);
        keys.forEach(key => {
            const option = document.createElement('option');
            option.value = key;
            option.text = key;
            selectElement.appendChild(option);
        });
    })
    .catch(error => {
        console.error('404!! ' + error);
    });

    fetch('data1.json')
    .then(response => response.json())
    .then(data1 => {
        const selectElement = document.getElementById('program');  
        selectElement.innerHTML = '<option value="default">-- Seçiniz --</option>';
        const keys = Object.keys(data1);
        keys.forEach(key => {
            const option = document.createElement('option');
            option.value = key;
            option.text = key;
            selectElement.appendChild(option);
        }); 
    })
    .catch(error => {
        console.error('404!! ' + error);
    });