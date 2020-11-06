
const tipCalculator = function(bill, service){

        return service == 'good' ? bill * .2
            :service == 'fair' ?  bill * .15
            :service == 'bad' ?  bill * .1
            :'Choice not valid'
}
tipCalculator(100, 'good')