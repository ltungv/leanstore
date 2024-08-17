package de.tu_darmstadt.systems;

import org.apache.bookkeeper.client.BKException;
import org.apache.bookkeeper.client.LedgerHandle;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class AsyncLedgerContext implements AutoCloseable {
    private static final Logger LOGGER = LoggerFactory.getLogger(AsyncLedgerContext.class);
    private final LedgerHandle ledgerHandle;
    private final List<CompletableFuture<Long>> onGoingRequests;

    public AsyncLedgerContext(LedgerHandle ledgerHandle) {
        this.ledgerHandle = ledgerHandle;
        this.onGoingRequests = new ArrayList<>();
    }

    public void appendAsync(byte[] data) {
        onGoingRequests.add(ledgerHandle.appendAsync(data));
        LOGGER.info("appending {}", data);
    }

    public long[] awaitAll() {
        CompletableFuture.allOf(onGoingRequests.toArray(new CompletableFuture[0])).join();
        List<Long> entryIDs = onGoingRequests.stream().map(CompletableFuture::join).toList();
        onGoingRequests.clear();
        return entryIDs.stream().mapToLong(Long::longValue).toArray();
    }

    @Override
    public void close() throws InterruptedException, BKException {
        this.ledgerHandle.close();
    }
}
