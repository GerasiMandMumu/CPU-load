function draw(lst, title, canvas_id) {
    let load = new Array();
    let time = new Array();

    for (let i = 1; i < lst.length; i++) {
        if(lst[i].fields['time'] - lst[i - 1].fields['time'] < 5){
            load.push(lst[i].fields['cpu_load']);
            time.push(lst[i].fields['time']);
        }
        else{
            load.push(0);
            time.push(lst[i].fields['time']);
        }

    }

    var Canvas = document.getElementById(canvas_id);
    Ctx = Canvas.getContext('2d');
    var chart = new Chart(Ctx, {
        type: 'bar',
        data:{
            labels: time,
            datasets:[{
                data: load,
                label: title,
                borderColor: "#3e95cd",
                backgroundColor: "#7bb6dd",
                fill: false,
                lineTension: 0,
            }]
        }
    });
}