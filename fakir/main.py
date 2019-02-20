
from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
import uvicorn
import json

from charts import get_chart_model

fakir = Starlette()


@fakir.route('/generator/{chartType}', methods=['GET'])
async def generator(request):

    chart_type = request.path_params['chartType']
    if chart_type not in get_chart_model.keys():
        return Response(f"'{chart_type}' is not a valide chartype", status_code=400)

    conf = await request.json()

    print(conf)

    ChartModel = get_chart_model[chart_type]
    data = ChartModel.parse_obj(conf).generateFakeData()

    return JSONResponse(json.loads(data.to_json(orient='records')), headers={
      "Access-Control-Allow-Origin": "*"
    })


@fakir.route('/jsonschemas/', methods=['GET'])
async def jsonschemas(request):

    json_schemas = {}
    for chart_type, ChartModel in get_chart_model.items():
        json_schemas[chart_type] = ChartModel.schema_json()

    return JSONResponse(json_schemas, headers={
      "Access-Control-Allow-Origin": "*"
    })


def test():
    json_schemas = {}
    for chart_type, ChartModel in get_chart_model.items():
        json_schemas[chart_type] = ChartModel.schema_json()

    return json_schemas


if __name__ == '__main__':
    uvicorn.run(fakir, host='0.0.0.0', port=8000)
