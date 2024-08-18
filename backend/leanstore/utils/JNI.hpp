#pragma once

#include "jni.h"

#include <string>
#include <vector>

std::string collectJarPaths();

namespace jni
{
void init(std::string&);
void deinit();

void attachThread();
void detachThread();

class JObjectRef
{
  protected:
   jobject object;

  public:
   friend jobject getJObject(JObjectRef&);

   JObjectRef(jobject);
   JObjectRef(const JObjectRef&);
   JObjectRef(JObjectRef&&);
   ~JObjectRef();

   JObjectRef& operator=(const JObjectRef&);
   JObjectRef& operator=(JObjectRef&&);

   template <typename... Args>
   jobject callNonVirtualObjectMethod(jclass, jmethodID, Args...);
};
}  // namespace jni

namespace java
{
namespace lang
{
class Throwable
{
  public:
   jni::JObjectRef ref;
   Throwable(jthrowable);
   std::string getMessage();
};
}  // namespace lang
}  // namespace java

namespace bookkeeper
{
class ClientConfiguration
{
  public:
   jni::JObjectRef ref;
   ClientConfiguration();
   ClientConfiguration& setMetadataServiceUri(std::string&);
};

class DigestType
{
  public:
   jni::JObjectRef ref;
   static DigestType CRC32();
   static DigestType CRC32C();
   static DigestType DUMMY();
   static DigestType MAC();
};

class BookKeeper
{
  public:
   jni::JObjectRef ref;
   BookKeeper(ClientConfiguration&);
   ~BookKeeper();
   jni::JObjectRef createLedger(int, int, DigestType&, char*, int);
};

class AsyncLedgerContext
{
  public:
   jni::JObjectRef ref;
   AsyncLedgerContext(jni::JObjectRef&);
   ~AsyncLedgerContext();

   void appendAsync(unsigned char*, int);
   std::vector<long> awaitAll();
};
}  // namespace bookkeeper
