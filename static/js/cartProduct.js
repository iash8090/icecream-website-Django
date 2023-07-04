$(document).ready(function(){

    $('.radio-group .radio').click(function(){
        $('.radio').addClass('gray');
        $(this).removeClass('gray');
    });
    
    $('.plus-minus .plus').click(function(){
        let sum=0;
        let count = $(this).parent().prev().text();
        let prd_id = this.id;
        $(this).parent().prev().html(Number(count) + 1);
        cart[prd_id][0] = Number(count) + 1;
        let qty = cart[prd_id][0];
        let prd_price = cart[prd_id][3];
        const ttl_price = qty * prd_price;
        cart[prd_id][5] = ttl_price;
        sessionStorage.setItem('cart', JSON.stringify(cart));
        $(this).parent().parent().parent().next().html(ttl_price);

        for (i in cart){
            sum += Number(cart[i][5]);
        }
        $("#tAmount").html(sum);

        
    });
    
    $('.plus-minus .minus').click(function(){
        let sum=0;
        let count = $(this).parent().prev().text();
        let prd_id = this.id;
        $(this).parent().prev().html(Math.max(1,Number(count) - 1));
        cart[prd_id][0] = Math.max(1, Number(count) - 1);
        let qty = cart[prd_id][0];
        let prd_price = cart[prd_id][3];
        const ttl_price = qty * prd_price;
        cart[prd_id][5] = ttl_price;
        sessionStorage.setItem('cart', JSON.stringify(cart))
        $(this).parent().parent().parent().next().html(ttl_price);

        for (i in cart){
            sum += Number(cart[i][5]);
        }
        $("#tAmount").html(sum);
    });

    $('.btn-close').click(function(){
        let prd_id = this.id;    
        delete cart[prd_id];
        sessionStorage.setItem('cart', JSON.stringify(cart))
        document.getElementById('cartcount').innerHTML = Object.keys(cart).length;
        location.reload();
    });
    
    });
