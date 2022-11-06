package com.smiles.server.controller;

import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.Struct;
import com.google.protobuf.util.JsonFormat;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.smiles.server.GetMoleculeRequest;
import com.smiles.server.MoleculeServiceGrpc;
import com.smiles.server.utils.StreamMoleculeJsonData;
import io.grpc.stub.StreamObserver;
import org.bson.Document;

import java.util.ArrayList;
import java.util.List;

public class MoleculeImpl extends MoleculeServiceGrpc.MoleculeServiceImplBase {
    String uri = "mongodb://localhost:27017";
    String dbName = "smilesDB";
    String collectionName = "Experimental Database";
    MongoClient connect = MongoClients.create(uri);
    MongoDatabase dbCursor = connect.getDatabase(dbName);
    MongoCollection<Document> dataCursor = dbCursor.getCollection(collectionName);

    List<Document> listOfMoleculeRecords = dataCursor.find().into(new ArrayList<>());

    @Override
    public void getMolecule(GetMoleculeRequest request, StreamObserver<Struct> responseObserver) {
        Struct.Builder structBuilder = Struct.newBuilder();
        try {
            JsonFormat.parser()
                .merge(StreamMoleculeJsonData.of(listOfMoleculeRecords).toJsonString(), structBuilder);
        } catch (InvalidProtocolBufferException e) {
            throw new RuntimeException(e);
        }
        System.out.println(listOfMoleculeRecords);
        responseObserver.onNext(structBuilder.build());
        responseObserver.onCompleted();
    }
}
