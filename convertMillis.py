# convertMillis


class convertMillis:
    def convertMillis(millis):
        millis = float(millis)
        seconds=(millis/1000.0)%60
        minutes=(millis/(1000*60))%60
        hours=(millis/(1000*60*60))%24
        output_format = f'{int(hours)}:{int(minutes)}:{int(seconds)}'

        return output_format
