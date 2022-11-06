package com.smiles.server.utils;

import org.bson.Document;

import java.util.List;
import java.util.stream.Collectors;

public class StreamMoleculeJsonData {
    private final List<Document> listOfMoleculeRecords;

    public StreamMoleculeJsonData(List<Document> listOfMoleculeRecords) {
        this.listOfMoleculeRecords = listOfMoleculeRecords;
    }

    public static StreamMoleculeJsonData of(List<Document> listOfMoleculeRecords){
        return new StreamMoleculeJsonData(listOfMoleculeRecords);
    }

    public String toJsonString(){
        return listOfMoleculeRecords
            .stream()
            .map(Document::toJson)
            .collect(Collectors.joining(",", "{\"data\": [", "]}"));
    }
}
