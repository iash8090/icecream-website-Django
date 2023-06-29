if (Object.keys(cart).length > 0 ){
    for (item in cart){
        let qty = cart[item][0];
        let prd_name = cart[item][1];
        let prd_img = cart[item][2];
        let prd_price = cart[item][3];
        mystr=`    <div class="row d-flex justify-content-center border-top">
            <div class="col-5">
                <div class="row d-flex">
                    <div>
                        <img src="${prd_img}" style="width:50%">
                    </div>
                    <div class="my-auto flex-column d-flex pad-left">
                        <h6 class="mob-text">${prd_name}</h6>
                    </div>
                </div>
            </div>
            <div class="my-auto col-7">
                <div class="row text-right">
                    <div class="col-3">
                        <p class="mob-text">${prd_price}</p>
                    </div>
                    <div class="col-3">
                        <div class="row d-flex justify-content-end px-3">
                            <p class="mb-0" id="cnt1">${qty}</p>
                            <div class="d-flex flex-column plus-minus">
                                <span class="fa fa-plus-square text-secondary plus"></span>
                                <span class="fa fa-minus-square text-secondary minus"></span>
                            </div>
                        </div>
                    </div>
                    <div class="col-3">
                        <h6 class="mob-text">${prd_price}</h6>
                    </div>
                    <div class="col-3">
                        <button type="button" class="btn-close" aria-label="Close"></button>
                    </div>
                </div>
            </div>
        </div>
        `
        $('#items').append(mystr);
    }

}
else{
mystr=`        <div class="card-body cart">
    <div class="col-sm-12 empty-cart-cls text-center">
        <img src="/static/img/emptyCart.png" width="130" height="130" class="img-fluid mb-4 mr-3">
        <h3><strong>Your Cart is Empty</strong></h3>
        <h4>Add something to make me happy :)</h4>
        <a href="/" class="btn btn-primary cart-btn-transform m-3" data-abc="true">continue shopping</a>
        
    
    </div>
</div>`

    $("#items").append(mystr)
    document.getElementById('tPrice').innerHTML= 0
}
