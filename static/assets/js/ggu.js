var click = document.querySelectorAll('.sidebar-item');

for(var i = 0; i < click.length; i++) {

    click[i].onclick = function() {
        console.log(event.currentTarget);

        var current = event.currentTarget;
        console.log(current);

        var li = document.querySelectorAll('.sidebar-item');
        for(var a = 0; a < li.length; a++) {

            if(li[a] === current) {
                current.classList.add('active');
            } else {
                li[a].classList.remove('active');
            }
        }
    }
}
