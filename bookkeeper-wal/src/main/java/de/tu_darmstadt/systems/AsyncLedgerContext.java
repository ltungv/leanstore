package de.tu_darmstadt.systems;

import org.apache.bookkeeper.client.BKException;
import org.apache.bookkeeper.client.LedgerHandle;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;

public class AsyncLedgerContext implements AutoCloseable {
    private final LedgerHandle ledgerHandle;
    private final List<CompletableFuture<Long>> onGoingRequests;

    public AsyncLedgerContext(LedgerHandle ledgerHandle) {
        this.ledgerHandle = ledgerHandle;
        this.onGoingRequests = new ArrayList<>();
    }

    public void appendAsync(byte[] data) {
        onGoingRequests.add(ledgerHandle.appendAsync(data));
    }

    public List<Long> awaitAll() {
        CompletableFuture.allOf(onGoingRequests.toArray(new CompletableFuture[0])).join();
        List<Long> entryIDs = onGoingRequests.stream().map(CompletableFuture::join).collect(Collectors.toList());
        onGoingRequests.clear();
        return entryIDs;
    }

    @Override
    public void close() throws InterruptedException, BKException {
        this.ledgerHandle.close();
    }
}
