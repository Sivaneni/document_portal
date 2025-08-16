import sys
from pathlib import Path
from src.multi_document_chat.data_ingestion import DocumentIngestor
from src.multi_document_chat.retrieval import ConversationalRAG

def test_document_ingestion_and_rag():
    try:
        test_files = [
             "data\\multi_doc_chat\\market_analysis_report.docx",
            "data\\multi_doc_chat\\NIPS-2017-attention-is-all-you-need-Paper.pdf",
            "data\\multi_doc_chat\\sample_1.pdf",
            "data\\multi_doc_chat\\state_of_the_union.txt"
        ]
        uploaded_files = []
        for file_path in test_files:
            if Path(file_path).exists():
                uploaded_files.append(open(file_path, "rb"))
            else:
                print(f"File does not exist: {file_path}")
                
        if not uploaded_files:
            print("No valid files to upload.")
            sys.exit(1)
            
        ingestor = DocumentIngestor()
        retriever = ingestor.ingest_files(uploaded_files)
        
        for f in uploaded_files:
            f.close()
                
        session_id = "test_multi_doc_chat"
        
        rag = ConversationalRAG(session_id=session_id, retriever=retriever)
        question = "what is attention is all you need paper about?"
        answer=rag.invoke(question)
        print("\n Question:", question)
        print("Answer:", answer)
        if not uploaded_files:
            print("No valid files to upload.")
            sys.exit(1)
    except Exception as e:
        print(f"Test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_document_ingestion_and_rag()
