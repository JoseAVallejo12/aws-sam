import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    data = event.get('body')

    if data is None or data.get('userNew') is None:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "use": "no ha funcionado !"
            })
        }

    print(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "userNew": "post_user(data)"
        })
    }


def post_user(data):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('customers')
    try:
        response = table.put_item(
            Item={
                'recency': data.get('userNew')[0]
                """ 'state': data.get('userNew')[1],
                'arrears_days': data.get('userNew')[2],
                'total_paid': data.get('userNew')[3],
                'monto_acum': data.get('userNew')[4],
                'uso_recursos': data.get('userNew')[5],
                'plazo': data.get('userNew')[6],
                'sector': data.get('userNew')[7],
                'ingresos': data.get('userNew')[8],
                'ubicacion': data.get('userNew')[9],
                'estrato_min': data.get('userNew')[10],
                'procesos_jud': data.get('userNew')[11],
                'alertas': data.get('userNew')[12],
                'score_bureau': data.get('userNew')[13],
                'huellas': data.get('userNew')[14],
                'website': data.get('userNew')[15],
                'instagram': data.get('userNew')[16],
                'linkedin_empresa': data.get('userNew')[17],
                'linkedin_empresarios': data.get('userNew')[18],
                'edad_empr': data.get('userNew')[19],
                'activador': data.get('userNew')[20],
                'numero_acc': data.get('userNew')[21],
                'impacto': data.get('userNew')[22],
                'acceso_banca': data.get('userNew')[23],
                'empleados': data.get('userNew')[24],
                'mujeres_empr': data.get('userNew')[25],
                'mujeres_cargos': data.get('userNew')[26], """
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
