import pandas as pd
import torch
from transformers import BertTokenizer, BertForTokenClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader
import numpy as np
import re




class KeywordDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        labels = self.labels[item]
        encoding = self.tokenizer(
            text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        encoding = {k: v.squeeze() for k, v in encoding.items()}

        # Create a binary label for each token
        label_ids = torch.zeros(self.max_len, dtype=torch.long)
        tokens = encoding['input_ids']
        for idx, token in enumerate(tokens):
            token_text = self.tokenizer.decode([token]).strip()
            if any(re.fullmatch(f".*{keyword}.*", token_text, re.IGNORECASE) for keyword in labels):
                label_ids[idx] = 1
        encoding['labels'] = label_ids
        return encoding
    





def predict_keywords(text, model, tokenizer, max_len=128):
    model.eval()
    encoding = tokenizer(
        text,
        max_length=max_len,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    with torch.no_grad():
        outputs = model(input_ids=encoding['input_ids'])

    logits = outputs.logits
    preds = torch.argmax(logits, dim=-1).squeeze().tolist()
    tokens = tokenizer.tokenize(text)
    keywords = [tokens[i] for i in range(max_len) if preds[i] == 1]
    return keywords



def main():

    # Load the dataset
    file_path = "training_data.csv"
    data = pd.read_csv(file_path)


    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    max_len = 128  # Define the max length for BERT input
    # Convert labels to list of lists
    data['Keywords'] = data['Keywords'].apply(lambda x: x.split(','))

    # Split dataset into training and validation
    train_texts, val_texts, train_labels, val_labels = train_test_split(
        data['Text'].tolist(),
        data['Keywords'].tolist(),
        test_size=0.2,
        random_state=42
    )

    # Create dataset objects
    train_dataset = KeywordDataset(train_texts, train_labels, tokenizer, max_len)
    val_dataset = KeywordDataset(val_texts, val_labels, tokenizer, max_len)

    model = BertForTokenClassification.from_pretrained("bert-base-uncased", num_labels=2)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer
    )

    trainer.train()


    sample_text = "What is the smallest positive integer that uses only the digits 0 and 2 in its notation and is divisible by 15?"
    keywords = predict_keywords(sample_text, model, tokenizer)
    print("Extracted Keywords:", keywords)



if __name__ == '__main__':
    main()