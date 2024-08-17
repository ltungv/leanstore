#pragma once

#include "jni.h"

#include <memory>
#include <string>
#include <vector>

std::string collectJarPaths();

namespace jni
{
void init(std::string&);
void deinit();

class JVMRef
{
  private:
   JavaVM* jvm;

  public:
   JVMRef(JavaVM*);
   ~JVMRef();
   JVMRef(const JVMRef&) = delete;
   JVMRef& operator=(const JVMRef&) = delete;
   JVMRef(JVMRef&&);
   JVMRef& operator=(JVMRef&&);
   JNIEnv* getEnv();
};

class JObjectRef
{
  protected:
   jobject object;

   JObjectRef(jobject);

  public:
   friend class LocalRef;
   friend class GlobalRef;
   friend jobject getJObject(JObjectRef&);

   virtual ~JObjectRef() = default;

   template <typename... Args>
   jobject callNonVirtualObjectMethod(jclass, jmethodID, Args...);
};

class LocalRef : public JObjectRef
{
  public:
   LocalRef(jobject);
   LocalRef(const LocalRef&) = delete;
   LocalRef(LocalRef&&);
   ~LocalRef() override;

   LocalRef& operator=(const LocalRef&) = delete;
   LocalRef& operator=(LocalRef&&);
};

class GlobalRef : public JObjectRef
{
  public:
   GlobalRef(LocalRef);
   GlobalRef(LocalRef&);
   GlobalRef(const GlobalRef&);
   GlobalRef(GlobalRef&&);
   ~GlobalRef() override;

   GlobalRef& operator=(const GlobalRef&);
   GlobalRef& operator=(GlobalRef&&);
};
}  // namespace jni

namespace java
{
namespace lang
{
class LocalThrowable
{
  public:
   jni::LocalRef ref;
   LocalThrowable(jthrowable);
   std::string getMessage();
};
}  // namespace lang
}  // namespace java

namespace bookkeeper
{
class LocalClientConfiguration
{
  public:
   jni::LocalRef ref;
   LocalClientConfiguration();
   LocalClientConfiguration& setMetadataServiceUri(std::string&);
};

class LocalDigestType
{
  public:
   jni::LocalRef ref;
   static LocalDigestType CRC32();
   static LocalDigestType CRC32C();
   static LocalDigestType DUMMY();
   static LocalDigestType MAC();
};

class GlobalBookKeeper
{
  public:
   jni::GlobalRef ref;
   GlobalBookKeeper(LocalClientConfiguration&);
   ~GlobalBookKeeper();
   jni::LocalRef createLedger(int, int, jni::JObjectRef&, char*, int);
};

class GlobalAsyncLedgerContext
{
  public:
   jni::GlobalRef ref;
   GlobalAsyncLedgerContext(jni::LocalRef&);
   ~GlobalAsyncLedgerContext();

   void appendAsync(char*, int);
   std::vector<long> awaitAll();
};
}  // namespace bookkeeper
