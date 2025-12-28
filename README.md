# DeepSeek OCR Project

This project leverages the **DeepSeek-OCR** model via **Ollama** to extract text and tables from PDF documents. It processes PDF pages by converting them to images and then running OCR to generate Markdown output.

## Features

- **PDF Processing**: Converts multi-page PDFs into individual images.
- **DeepSeek-OCR Integration**: Uses the `deepseek-ocr:latest` model running locally on Ollama.
- **Markdown Output**: Generates Markdown files for each page and a combined result.
- **Table Extraction**: Optimized prompts to extract data as HTML tables within Markdown.

## Prerequisites

- **Python 3.8+**
- **Ollama**: Installed and running locally.
- **DeepSeek OCR Model**: `deepseek-ocr:latest` pulled in Ollama.
  ```bash
  ollama pull deepseek-ocr:latest
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd deepocr
   ```

2. Install Python dependencies:
   ```bash
   pip install ollama pymupdf
   ```

## Usage

1. Place your PDF file in the project directory (e.g., `deepseekocr.pdf`).
2. Update the `pdf_file` variable in `pdf_processor.py` if needed.
3. Run the processor:
   ```bash
   python pdf_processor.py
   ```
4. Find the output in the `deepseek_extraction` directory.

## File Structure

- `ollama_ocr.py`: Handles the interface with the Ollama API for OCR.
- `pdf_processor.py`: Main script to handle PDF conversion and orchestration.
