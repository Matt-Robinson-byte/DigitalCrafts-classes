
const tipCalculator = function(bill, service){

    return service == 'good' ? bill * .2 + bill
        :service == 'fair' ?  bill * .15 + bill
        :service == 'bad' ?  bill * .1 + bill
        :'Choice not valid'
}
tipCalculator(100, 'good')