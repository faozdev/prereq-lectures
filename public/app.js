fetch('faculty_programs.json')
    .then(response => response.json())
    .then(data => {
        const selectElement = document.getElementById('faculty');
        const programSelectElement = document.getElementById('program');
        selectElement.innerHTML = '<option value="default">-- Seçiniz --</option>';
        const keys = Object.keys(data);
        keys.forEach(key => {
            const option = document.createElement('option');
            option.value = key;
            option.text = key;
            selectElement.appendChild(option);
        });
        function updatePrograms() {
            const selectedFaculty = selectElement.value;
            programSelectElement.innerHTML = '<option value="default">-- Seçiniz --</option>';
            if (selectedFaculty !== 'default') {
                const programs = data[selectedFaculty];
                programs.forEach(program => {
                    const option = document.createElement('option');
                    option.value = program;
                    option.text = program;
                    programSelectElement.appendChild(option);
                });
            }
        }
        
        selectElement.addEventListener('change', updatePrograms); 
        
    })
    

document.addEventListener('DOMContentLoaded', function() {
    const myButton = document.getElementById('Goster');
    if (myButton) {
        myButton.addEventListener('click', function() {
            var iterationFormValue = document.getElementById("program").value;
            
            fetch('/curriculum', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ iterationFormValue }),
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Hata:', error);
                });
            });
    }
});
        
        
        
        
                




