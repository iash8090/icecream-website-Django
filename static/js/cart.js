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
    </div>`
    $('#items').append(mystr);
}

