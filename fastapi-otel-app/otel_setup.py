from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

resource = Resource(attributes={SERVICE_NAME: "real-fastapi-app"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer_provider = trace.get_tracer_provider()

#otlp_exporter = OTLPSpanExporter(endpoint="http://otelcol-opentelemetry-collector.observability-horizon-relevance.svc.cluster.local:4318", insecure=True)
otlp_exporter = OTLPSpanExporter(endpoint="http://otelcol-opentelemetry-collector.observability-horizon-relevance.svc.cluster.local:4318")


tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
