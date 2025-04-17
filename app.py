import logging
import time
from opentelemetry import _logs
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# Set up OpenTelemetry logging
def setup_logging():
    # Create a logger provider
    logger_provider = LoggerProvider()

    # Set up OTLP log exporter to send logs to the OTel Collector
    otlp_exporter = OTLPLogExporter(
        endpoint="http://otel-collector:4317",  # OTel Collector endpoint
        insecure=True,  # Use insecure connection (no TLS)
    )

    # Add the OTLP exporter to the logger provider
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))

    # Set the global logger provider
    _logs.set_logger_provider(logger_provider)

    # Configure Python logging to use OpenTelemetry
    handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

# Main function to generate logs
def generate_logs():
    count = 0
    while True:
        try:
            count += 1
            # Generate log messages
            logging.info(f"This is a test INFO log message #{count}")
            logging.error(f"This is a test ERROR log message #{count}")
            print(f"Generated log #{count}")  # Print to console for debugging

            # Wait for 1 second before generating the next log
            time.sleep(1)
        except Exception as e:
            print(f"Error in log generation: {e}")
            time.sleep(5)

# Entry point
if __name__ == "__main__":
    # Set up OpenTelemetry logging
    setup_logging()

    # Start generating logs
    print("Starting log generation...")
    generate_logs()