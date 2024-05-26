# from transformers import BertForTokenClassification, BertTokenizer, TrainingArguments, Trainer
from transformers import BertForTokenClassification, BertTokenizerFast, TrainingArguments, Trainer
from datasets import Dataset, DatasetDict
import numpy as np
import torch

# Define your tokenized input and labels
data = {
    "tokens": [
        ["What", "is", "the", "smallest", "positive", "integer", "that", "uses", "only", "the", "digits", "$0$", "and", "$2$", "in", "its", "notation", "and", "is", "divisible", "by", "$15$"]
    ],
    "tags": [
        ["O", "O", "O", "O", "B-KEY", "E-KEY", "O", "O", "O", "O", "B-KEY", "O", "O", "O", "O", "O", "B-KEY", "O", "O", "B-KEY", "O", "O"]

    ]
}

# Create Dataset
dataset = Dataset.from_dict(data)

# Preprocess the data
model_name = "bert-base-uncased"
tokenizer = BertTokenizerFast.from_pretrained(model_name)

def encode_tags(tags, encodings):
    labels = [[tag2id[tag] for tag in doc] for doc in tags]
    encoded_labels = []
    for doc_labels, doc_offset in zip(labels, encodings["offset_mapping"]):
        # Create an empty array of -100
        doc_enc_labels = np.ones(len(doc_offset), dtype=int) * -100
        arr_offset = np.array(doc_offset)
        # Set labels whose first offset position is 0 and the second is not 0
        doc_enc_labels[(arr_offset[:, 0] == 0) & (arr_offset[:, 1] != 0)] = doc_labels
        encoded_labels.append(doc_enc_labels.tolist())

    return encoded_labels

# Convert tags to ids
unique_tags = set(tag for doc in data["tags"] for tag in doc)
tag2id = {tag: id for id, tag in enumerate(unique_tags)}
id2tag = {id: tag for tag, id in tag2id.items()}

# Tokenize inputs
encodings = tokenizer(data['tokens'], is_split_into_words=True, return_offsets_mapping=True, padding=True, truncation=True)
labels = encode_tags(data['tags'], encodings)
encodings.pop("offset_mapping")  # we don't want to pass this to the model


# Create Dataset object
# class NERDataset(Dataset):
#     def __init__(self, encodings, labels):
#         self.encodings = encodings
#         self.labels = labels

#     def __getitem__(self, idx):
#         item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
#         item['labels'] = torch.tensor(self.labels[idx])
#         return item

#     def __len__(self):
#         return len(self.labels)

# ner_dataset = NERDataset(encodings, labels)


# Add encodings and labels to the dataset
# dataset = dataset.add_column("input_ids", [enc["input_ids"] for enc in encodings.encodings])
# dataset = dataset.add_column("attention_mask", [enc["attention_mask"] for enc in encodings.encodings])
# dataset = dataset.add_column("labels", labels)

# Extract the tokenized data correctly

input_ids = encodings["input_ids"]
attention_masks = encodings["attention_mask"]

# Reconstruct dataset with necessary fields
dataset = dataset.add_column("input_ids", input_ids)
dataset = dataset.add_column("attention_mask", attention_masks)
dataset = dataset.add_column("labels", labels)


# Load the pre-trained model
model = BertForTokenClassification.from_pretrained(model_name, num_labels=len(tag2id))

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Train model
trainer.train()

# Test the model on a new sequence of tokens
test_sentence = ["Which", "non-negative", "integer", "has", "the", "property", "that", "the", "sum", "of", "its", "digits", "is", "15?"]

# Tokenize test sentence
test_encodings = tokenizer(test_sentence, is_split_into_words=True, return_tensors="pt", padding=True, truncation=True)

# Make predictions
model.eval()
with torch.no_grad():
    outputs = model(**test_encodings)
    predictions = torch.argmax(outputs.logits, dim=2)

# Convert predictions to tags
predicted_tags = [id2tag[id.item()] for id in predictions[0]]

# Combine tokens and their predicted tags
token_tag_pairs = list(zip(test_sentence, predicted_tags))

# Print out the results
for token, tag in token_tag_pairs:
    print(f"{token} ({tag})")


