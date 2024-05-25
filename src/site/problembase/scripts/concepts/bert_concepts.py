import pandas as pd
from transformers import BertTokenizerFast, BertForTokenClassification, Trainer, TrainingArguments, pipeline
from datasets import Dataset

# Example data
data = {
    "sentences": [
        "The result of 3 plus 5 is 8.",
        "You can calculate 9 minus 4 easily.",
        "Multiplying 6 by 7 gives you 42.",
        "If you divide 15 by 3, you get 5."
    ],
    "labels": [
        ["O", "O", "O", "O", "B-ADD", "O", "O", "O"],
        ["O", "O", "O", "O", "B-SUB", "O", "O", "O"],
        ["B-MUL", "O", "O", "O", "I-MUL", "O", "O", "O"],
        ["O", "O", "B-DIV", "O", "O", "I-DIV", "O", "O", "O"]
    ]
}

df = pd.DataFrame(data)

# Load the tokenizer
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

# Tokenize the sentences
tokenized_inputs = tokenizer(df["sentences"].tolist(), truncation=True, is_split_into_words=True)

# Function to align labels with tokenized inputs
def align_labels_with_tokens(labels, tokenized_inputs):
    new_labels = []
    for i, label in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_id = None
        label_ids = []
        for word_id in word_ids:
            if word_id is None:
                label_ids.append(-100)
            elif word_id != previous_word_id:
                label_ids.append(label[word_id])
            else:
                label_ids.append(label[word_id] if label[word_id].startswith("I") else "I" + label[word_id][1:])
            previous_word_id = word_id
        new_labels.append(label_ids)
    return new_labels

aligned_labels = align_labels_with_tokens(data["labels"], tokenized_inputs)
tokenized_inputs["labels"] = aligned_labels

# Convert the tokenized inputs to a Dataset
dataset = Dataset.from_dict(tokenized_inputs)

# Define the label list
label_list = ["O", "B-ADD", "I-ADD", "B-SUB", "I-SUB", "B-MUL", "I-MUL", "B-DIV", "I-DIV"]

# Load the model
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=len(label_list))

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=dataset,  # In a real scenario, use a separate eval dataset
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("./fine-tuned-bert-math")
tokenizer.save_pretrained("./fine-tuned-bert-math")

# Load the fine-tuned model and tokenizer for inference
model = BertForTokenClassification.from_pretrained("./fine-tuned-bert-math")
tokenizer = BertTokenizerFast.from_pretrained("./fine-tuned-bert-math")

# Create a pipeline for token classification
nlp = pipeline("token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Example text for keyword detection
text = "To solve 12 plus 7, you add them together."

# Predict keywords
predictions = nlp(text)

# Extract keywords
keywords = [pred['word'] for pred in predictions if pred['entity'].startswith("B-") or pred['entity'].startswith("I-")]

print(keywords)
