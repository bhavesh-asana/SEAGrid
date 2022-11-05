package com.smiles.server.utils;

import org.bson.Document;

import java.util.List;
import java.util.stream.Collectors;

public class StreamJsonData {
    private final List<Document> listOfMoleculeRecords;

    public StreamJsonData(List<Document> listOfMoleculeRecords) {
        this.listOfMoleculeRecords = listOfMoleculeRecords;
    }
    public static StreamJsonData of(List<Document> listOfMoleculeRecords){
        return new StreamJsonData(listOfMoleculeRecords);
    }

    public String toJsonString(){
        return listOfMoleculeRecords
            .stream()
            .map(Document::toJson)
            .collect(Collectors.joining(",", "{\"data\": [", "]}"));
    }
}
