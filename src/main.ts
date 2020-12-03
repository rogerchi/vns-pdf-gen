import * as cdk from '@aws-cdk/core';
import * as api from '@aws-cdk/aws-apigatewayv2';
import * as integrations from '@aws-cdk/aws-apigatewayv2-integrations';
import * as python from '@aws-cdk/aws-lambda-python';
import * as lambda from '@aws-cdk/aws-lambda';
import * as path from 'path';

export class VnsPdfGenerator extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: cdk.StackProps = {}) {
    super(scope, id, props);

    const vnsFunc = new python.PythonFunction(this, 'VnsFunc', {
      entry: path.join(__dirname, 'vns'),
      runtime: lambda.Runtime.PYTHON_3_8,
      memorySize: 1024,
      timeout: cdk.Duration.seconds(25),
    });

    const httpApiIntegration = new integrations.LambdaProxyIntegration({
      payloadFormatVersion: api.PayloadFormatVersion.VERSION_2_0,
      handler: vnsFunc,
    });

    const httpApi = new api.HttpApi(this, 'HttpApi');

    httpApi.addRoutes({
      path: '/',
      methods: [api.HttpMethod.GET],
      integration: httpApiIntegration,
    });

    new cdk.CfnOutput(this, 'Api', {
      value: httpApi.apiEndpoint,
    });
  }
}

// for development, use account/region from cdk cli
const devEnv = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const app = new cdk.App();

new VnsPdfGenerator(app, 'vns-pdf-gen', { env: devEnv });
// new MyStack(app, 'my-stack-prod', { env: prodEnv });

app.synth();
