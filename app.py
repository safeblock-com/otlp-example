from flask import Flask

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)

resource = Resource(attributes={"service.name": "example_service"})

otlp_exporter = OTLPSpanExporter(insecure=True)
tracer_provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

FlaskInstrumentor().instrument_app(app)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
