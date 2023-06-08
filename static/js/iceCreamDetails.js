function CalcAmount(qt)
{
    var ttl_price = qt * document.getElementById('dynamicPrice').innerHTML;
    var T_price = document.getElementById('Total_price');
    T_price.value=ttl_price;
}