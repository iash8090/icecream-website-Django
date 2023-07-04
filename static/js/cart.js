if (Object.keys(cart).length > 0 ){

    let sum = 0;
    for (item in cart){
        sum += Number(cart[item][5]);
        let qty = cart[item][0];
        let prd_name = cart[item][1];
        let prd_img = cart[item][2];
        let prd_price = cart[item][3];
        let slug_name = cart[item][4];
        let prd_ttl_price = qty * prd_price;
        cart[item][5] = prd_ttl_price;
        sessionStorage.setItem('cart', JSON.stringify(cart));
        mystr=`    <div class="row d-flex justify-content-center border-top">
            <div class="col-5">
                <div class="row d-flex">
                    <div>
                    <a href="/icd/${slug_name}">
                        <img src="${prd_img}" style="width:50%">
                        </a>
                    </div>
                    <div class="my-auto flex-column d-flex pad-left py-2">
                        <h6 class="mob-text">${prd_name}</h6>
                    </div>
                </div>
            </div>
            <div class="my-auto col-7">
                <div class="row text-right">
                    <div class="col-3">
                        <p class="mob-text" id="dynamicPrice">${prd_price}</p>
                    </div>
                    <div class="col-3">
                        <div class="row d-flex justify-content-end px-3">
                            <p class="qty mb-0" id="cnt1">${qty}</p>
                        <div class="d-flex flex-column plus-minus">
                            <span class="fa fa-plus-square text-secondary plus" id="${item}"></span>
                            <span class="fa fa-minus-square text-secondary minus" id="${item}"></span>
                        </div>
                    </div>

                    </div>
                    <div class="col-3">
                    <p class="Total_price mob-text" id="Total_price"> ${prd_ttl_price}</p>
                    </div>
                    <div class="col-3">
                        <button type="button" class="btn-close" aria-label="Close" id="${item}"></button>
                    </div>
                </div>
            </div>
        </div>
        `
        $('#items').append(mystr);
        
    }
    $("#tAmount").html(sum);


}
else{
    let sum = 0
    mystr=`        <div class="card-body cart">
        <div class="col-sm-12 empty-cart-cls text-center">
            <img src="/static/img/emptyCart.png" width="130" height="130" class="img-fluid mb-4 mr-3">
            <h3><strong>Your Cart is Empty</strong></h3>
            <h4>Add something to make me happy :)</h4>
            <a href="/" class="btn btn-primary cart-btn-transform m-3" data-abc="true">continue shopping</a>
            
        
        </div>
    </div>`

    $("#items").append(mystr)
    $("#tAmount").html(sum);
}
